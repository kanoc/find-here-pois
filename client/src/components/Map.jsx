import React from 'react'
import { connect } from 'react-redux'
import PigeonMap from 'pigeon-maps'
import PigeonMarker from 'pigeon-marker'
import { changeBbox, selectItem } from '../store/actions'

const mapDispatchToProps = dispatch => ({
    changeBbox: bbox => dispatch(changeBbox(bbox)),
    selectHotel: itemId => dispatch(selectItem(itemId)),
});

const mapStateToProps = state => {
    return {
        hotels: state.hotels
    };
};

const ConnectedMap = ({ hotels, changeBbox, selectHotel }) => {

    const onBoundsChanged = ({ bounds }) => {
        const bbox = [bounds.sw[1], bounds.sw[0], bounds.ne[1], bounds.ne[0]];
        changeBbox(bbox)
    };

    const handleMarkerClick = ({ payload }) => {
        selectHotel(payload);
    };

    return (
        <PigeonMap
            center={[48.137154, 11.576124]}
            zoom={12}
            animate={true}
            mouseEvents={true}
            touchEvents={true}
            onBoundsChanged={onBoundsChanged}>
            {hotels.map(item => (
                <PigeonMarker key={item.id} anchor={[item.position.lat, item.position.lon]} payload={item.id} onClick={handleMarkerClick} />
            ))}
        </PigeonMap>
    );
};

export default connect(mapStateToProps, mapDispatchToProps)(ConnectedMap);
