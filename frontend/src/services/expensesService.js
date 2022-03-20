import moment from "moment";
import 'moment-duration-format';
import apiService from "./apiService";

const base_url = env?.API_URL;

class ExpensesService {
    getExpenses(start_date = '2022-01-01T15:00:00-03:00', end_date = '2022-01-31T16:00:00-03:00') {
        if(start_date){
            start_date = moment(start_date).format('YYYY-MM-DD');
        }
        if(end_date){
            end_date = moment(end_date).format('YYYY-MM-DD');
        }
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}expenses?start_date=${start_date}&end_date=${end_date}`;
            let response = await fetch(endpoint);
            let expenses = await response.json();
            let formatedExpenses = this.formatExpenses(expenses);
            resolve(formatedExpenses)
        });
    }

    formatExpenses(expenses) {
        return expenses;
    }

    newExpense (expense) {
        if(expense.start){
            expense.start = moment(expense.start).format('YYYY-MM-DD');
        }
        if(expense.end){
            expense.end = moment(expense.end).format('YYYY-MM-DD');
        }
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}expenses/`;
            let response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(expense)
            });
            let r = await response.json();
            resolve({result: r})
        });
    }
    deleteExpense (expense_id) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}expenses/${expense_id}`;
            let response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });
            let r = await response.json();
            resolve({result: r})
        });
    }
    editExpense(id, expense) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}expenses/${id}/`;
            let response = await fetch(endpoint, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(expense)
            });
            let r = await response.json();
            resolve({result: r})
        });
    }

    getExpensesOptions() {
        return new Promise(async (resolve, reject) => {
            const endpoint = `expensesoptions/`;
            const r = await apiService.get(endpoint);
            resolve(r)
        });
    }

    getPayments(start_date, end_date) {
        if(start_date){
            start_date = moment(start_date).format('YYYY-MM-DD');
        }
        if(end_date){
            end_date = moment(end_date).format('YYYY-MM-DD');
        }
        return new Promise(async (resolve, reject) => {
            const endpoint = `payments?start_date=${start_date}&end_date=${end_date}`;
            const payments = await apiService.get(endpoint);
            const r = await this.formatPaymentsByPeriodAndExpense(payments)
            resolve(r)
        });
    }
    getKeyFromPayment (payment, full) {
        full = full ?? true;
        let date = new Date(payment.date);
        let dateWithoutOffset = new Date(date.getTime() + date.getTimezoneOffset() * 60000);
        let key = dateWithoutOffset.toLocaleString('default', { month: 'short', year: 'numeric' });
        return full ? key + payment.expense : key;
    }
    refreshPayments (payments) {
        return new Promise(async (resolve, reject) => {
            for(let period in payments){
                if(!payments[period].expense){
                    payments[period] = {
                        total : 0,
                        estimated : 0,
                        hoursValue: 0,
                        hours : 0,
                        diference: 0,
                    }
                }
            }
            for(let period in payments){
                if(payments[period].expense){
                    let key = this.getKeyFromPayment(payments[period], false);
                    payments[key] = {
                        total : (payments[key]?.total ?? 0) + payments[period].amount,
                        estimated : (payments[key]?.estimated ?? 0) + Number(payments[period].estimated),
                        hoursValue: payments[period].hoursValue,
                        hours : (payments[key]?.hours ?? 0) + payments[period].amount/ payments[period].hoursValue,
                        diference: (payments[key]?.diference ?? 0) + (payments[period].estimated - payments[period].amount),
                    }
                }
            }
            resolve(payments);
        });
    }
    formatPaymentsByPeriodAndExpense(payments) {
        return new Promise((resolve, reject) => {
           const ret = payments.map( p => ({
                ...p,
                amount: Number(p.amount),
                estimated : Number(p.estimated),
                hoursValue: Number(p.hoursValue),
            })).reduce((acc, p) => {
                let keyFull =this.getKeyFromPayment(p);
                let key = this.getKeyFromPayment(p, false);
                let accTotal =  acc[key]?.total || 0;
                let accEstimated = acc[key]?.estimated || 0;
                let accHours = acc[key]?.hours || 0;
                let accDiference = acc[key]?.diference || 0;
                return {
                    ...acc,
                    [keyFull]: {
                        ...p
                    },
                    [key]: {
                        total : accTotal + p.amount,
                        estimated : accEstimated + p.estimated,
                        hoursValue: p.hoursValue,
                        hours : accHours + p.amount/ p.hoursValue,
                        diference: accDiference + (p.estimated - p.amount),
                    }
                }
            }, {});
            resolve(ret);
        });
    }

    newPayment(payment, files) {
        return new Promise(async (resolve, reject) => {
            let headers = {'Accept': 'application/json'}
            const endpoint = `payments/`;
            let data = new FormData();
            if(typeof files !== 'undefined' && files.length > 0){
                let file = files[0];
                data.append('voucher', file);
                headers = {...headers, 'Content-Disposition': 'attachment', 'filename': file.name}
            }
            for(var key in payment){
                if(key === 'date'){
                    payment[key] = moment(payment[key]).format('YYYY-MM-DD');
                }
                data.append(key, payment[key]);
            }
            
            const r  =await apiService.post(endpoint, data, headers);
            resolve(r)
        });
    }

    deletePayment(payment_id) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `payments/${payment_id}`;
            const r = await apiService.delete(endpoint);
            resolve({result: r})
        });
    }

    editPayment(id, payment, files) {
        return new Promise (async (resolve, reject) => {
            let headers = {'Accept': 'application/json'}
            const endpoint = `payments/${id}/`;
            let data = new FormData();
            if(typeof files !== 'undefined' && files.length > 0){
                let file = files[0];
                data.append('voucher', file);
                headers = {...headers, 'Content-Disposition': 'attachment', 'filename': file.name}
            }
            for(var key in payment){
                if(key === 'date'){
                    payment[key] = moment(payment[key]).format('YYYY-MM-DD');
                }
                if(key !== 'voucher'){
                    data.append(key, payment[key]);
                }
            }
            const r = await apiService.put(endpoint, data, headers);
            resolve(r)    
        });
    }
}
const expensesService = new ExpensesService();
export default expensesService;