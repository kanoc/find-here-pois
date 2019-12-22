import { BBOX_CHANGED, ITEM_SELECTED } from "./action-types";

export const changeBbox = (bbox) => {
    return { type: BBOX_CHANGED, bbox: bbox };
};

export const selectItem = (itemId) => {
    return { type: ITEM_SELECTED, itemId: itemId };
};
