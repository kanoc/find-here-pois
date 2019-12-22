import { takeLatest, call, put } from 'redux-saga/effects';
import { BBOX_CHANGED, DATA_LOADED, API_ERRORED } from './action-types';
import Api from "./Api"

export default function* watcherSaga() {
    yield takeLatest(BBOX_CHANGED, loadData);
}

function* loadData(action) {
    try {
        const payload = yield call(getData, action.bbox);
        yield put({ type: DATA_LOADED, payload: payload });
    } catch (e) {
        console.log('Error loading data: ', e);
        yield put({ type: API_ERRORED, error: e });
    }
}

function getData(bbox) {
    return Api.getHotels(bbox).then(response => response.json());
}
