const API_BASE_URL = 'http://localhost:9000';

export default class Api {

    static getHotels(bbox, limit = 50) {
        const urlParams = objectToQs({bbox: bbox.toString(), limit: limit});
        const url = `${API_BASE_URL}/api/hotels?${urlParams}`;
        return fetch(url, { method: 'GET' });
    }

}

function objectToQs(obj) {
    return Object.keys(obj).map(key => key + '=' + obj[key]).join('&');
}
