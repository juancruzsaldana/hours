import apiService from "./apiService";

class AcccesService {
    getAccess() {
        return new Promise(async (resolve, reject) => {
            const endpoint = `access/`;
            const r = await apiService.get(endpoint);
            resolve(r)
        });
    }

    newAccess(access) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `access/`;
            const r = await apiService.post(endpoint, JSON.stringify(access));
            resolve(r)
        });
    }

    editAccess (id, {service, url, user, password, observations}) {
        // const id = access.id;
        // delete access.id;
        return new Promise(async (resolve, reject) => {
            const endpoint = `access/${id}/`;
            const r = await apiService.put(endpoint, JSON.stringify({service, url, user, password, observations}));
            resolve(r)
        });
    }

    removeAccess (id) {
        return new Promise(async (resolve, reject) => {
            const endpoint = `access/${id}/`;
            const r = await apiService.delete(endpoint);
            resolve(r)
        });
    }
}

const accessService = new AcccesService();
export default accessService;