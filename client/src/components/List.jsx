import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import ListItem from './ListItem'
import { selectItem } from "../store/actions";

const ListContainer = styled.div`
    display: flex;
    flex-direction: column;
    text-align: left;
    width: 408px;
    box-shadow: 0 4px 10px -2px rgba(0, 0, 0, 0.5);
    z-index: 5;
    overflow-y: auto;
`;

const ListHeader = styled.span`
    font-weight: bold;
    padding: 10px 18px 20px 24px;
`;

const Divider = styled.hr`
    width: 100%;
    height: 0;
    margin:0;
    padding:0;
    border: 0;
    border-bottom: 1px solid #e9e9e9;
    overflow: hidden;
`;

const mapStateToProps = state => ({
    hotels: state.hotels,
    selectedId: state.selectedId
});

const mapDispatchToProps = dispatch => ({
    selectHotel: itemId => dispatch(selectItem(itemId)),
});

const ConnectedList = ({ hotels, selectedId, selectHotel }) => {

    const onItemClick = (itemId) => {
        selectHotel(itemId)
    };

    const headerText = hotels.length >= 1
        ? "An exquisite selection of wonderful hotels in the area:"
        : "No hotels found in the area. Zoom in/out or move the map around!";

    return (
        <ListContainer>
            <ListHeader>{headerText}</ListHeader>
            {hotels.map(item => (
                <React.Fragment key={item.id}>
                    <Divider/>
                    <ListItem key={item.id} item={item} isSelected={item.id === selectedId} onItemClick={onItemClick}/>
                </React.Fragment>
            ))}
        </ListContainer>
    );
};


export default connect(mapStateToProps, mapDispatchToProps)(ConnectedList);
