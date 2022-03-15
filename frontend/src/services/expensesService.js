import moment from "moment";
import 'moment-duration-format';
const base_url = env?.API_URL;

class ExpensesService {
    getExpenses(start_date = '2022-01-01T15:00:00-03:00', end_date = '2022-01-31T16:00:00-03:00') {
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
}
const expensesService = new ExpensesService();
export default expensesService;