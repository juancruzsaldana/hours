import apiService from "./apiService";
import moment from "moment";
class DollarsService {
    getMovements() {
        return new Promise(async (resolve, reject) => {
            const endpoint = `dollars/`;
            const movemets = await apiService.get(endpoint);
            const r = this.mapMovements(movemets);
            resolve(r);
        });
    }
    mapMovements(movements) {
        let partialAcum = 0;
        const totals = {
            totalDebit: 0,
            totalCredit: 0,
            totalInPesos: 0,
            quoteAvg: 0,
            totalBalance: 0,
            totalBalanceInPesos: 0,
            lastPartial : 0,
        };
        const mappedMovements = movements.map(movement => {
            const { amountInDollars, amountInPesos, date, name, type, type_choices, get_type_display, id, sellValue } = movement;
            const newMovement = {
                id,
                amountInDollars: type === '1'?  Number(amountInDollars) : Number(amountInDollars) * -1,
                amountInPesos: type === '1'? Number(amountInPesos) : Number(amountInPesos) * -1,
                date : moment(date).format('DD/MM/YYYY'),
                name,
                type,
                partial: partialAcum += type === '1'? Number(amountInDollars): Number(amountInDollars) * -1,
                quote: Number(amountInPesos) / Number(amountInDollars),
                type_choices,
                get_type_display,
                sellValue
            };
            totals.totalCredit += type === '1'? Number(amountInDollars): 0;
            totals.totalDebit += type === '2'? Number(amountInDollars): 0;
            totals.totalInPesos += type === '1'? Number(amountInPesos) : Number(amountInPesos) * -1;
            totals.lastPartial = newMovement.partial;
            return newMovement;
        });
        totals.quoteAvg = totals.totalInPesos / (totals.totalCredit - totals.totalDebit) ;
        return {movements: mappedMovements.reverse(), totals};
    }

    newMovement(movement) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `dollars/`;
            movement.date = moment(movement.date).format('YYYY-MM-DD');
            const r = await apiService.post(endpoint, JSON.stringify(movement));
            resolve(r)
        });
    }

    getSources() {
        return new Promise(async (resolve, reject) => {
            const endpoint = `source/`;
            const r = await apiService.get(endpoint);
            resolve(r)
        });
    }

    newSource(source) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `source/`;
            const r = await apiService.post(endpoint, JSON.stringify(source));
            resolve(r)
        });
    }

    editSource (id, {name,description, amount}) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `source/${id}/`;
            const r = await apiService.put(endpoint, JSON.stringify({name,description, amount}));
            resolve(r)
        });
    }

    removeSource (id) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `source/${id}/`;
            const r = await apiService.delete(endpoint);
            resolve(r)
        });
    }

    getMovementDetails (movementId) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `movementDetails/${movementId}/`;
            const r = await apiService.get(endpoint);
            resolve(r)
        });
    }

    newMovementDetail (detail) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `movementDetails/`;
            const r = await apiService.post(endpoint, JSON.stringify(detail));
            resolve(r)
        });
    }
    
}

const dollarsService = new DollarsService();
export default dollarsService;