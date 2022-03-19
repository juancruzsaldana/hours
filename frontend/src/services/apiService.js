import {base_url} from "./appConfigService";
class ApiService {
    get(endpoint, data) {
        return new Promise(async (resolve, reject) => {
            let response = await fetch(`${base_url}${endpoint}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: data
            });
            let r = await response.json();
            resolve(r);
        });
    }

    post(endpoint, data, headers) {
        headers = headers ?? {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };
        return new Promise(async (resolve, reject) => {
            let response = await fetch(`${base_url}${endpoint}`, {
                method: 'POST',
                headers: headers,
                body: data
            });
            let r = await response.json();
            resolve(r);
        });
    }

    put(endpoint, data, headers) {
        headers = headers ?? {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };
        return new Promise(async (resolve, reject) => {
            let response = await fetch(`${base_url}${endpoint}`, {
                method: 'PUT',
                headers: headers,
                body: data
            });
            let r = await response.json();
            resolve(r);
        });
    }

    delete(endpoint) {
        return new Promise(async (resolve, reject) => {
            let response = await fetch(`${base_url}${endpoint}`, {
                method: 'DELETE',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
            });
            let r = await response.json();
            resolve(r);
        });
    }
}
const apiService = new ApiService();
export default apiService;