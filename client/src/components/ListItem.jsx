import React from 'react';
import styled from 'styled-components';

const ListElement = styled.div`
    cursor: pointer;
    padding: 10px 18px 10px 24px;
    &:hover {
        background-color: #e9e9e9;
    }
    background: ${props => props.isSelected ? '#aaa' : '#fff' };
  }
`;

const ListItem = ({ item, isSelected, onItemClick }) => {

    const handleOnClick = () => {
        onItemClick(item.id)
    };

    return (
        <ListElement onClick={handleOnClick} isSelected={isSelected}>
            <div>{item.title}</div>
            <div><i>Rating: {item.rating}</i></div>
        </ListElement>
    )};

export default ListItem
