const API_BASE_URL = process.env.NODE_ENV === 'development'
    ? 'http://localhost:9000'
    : 'https://find-here-pois-api.herokuapp.com/';

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
