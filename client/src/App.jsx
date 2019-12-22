import React from 'react';
import styled from 'styled-components';

import Map from './components/Map';
import List from './components/List'

const HorizontalContainer = styled.div`
    display: flex;
    flex-direction: row;
`;

const data = [
  {
    id: 'a',
    title: 'Robin',
  },
  {
    id: 'b',
    title: 'Dave',
  },
  {
    id: 'c',
    title: 'Dave',
  },
  {
    id: 'd',
    title: 'Dave',
  },
  {
    id: 'e',
    title: 'Dave',
  },
  {
    id: 'f',
    title: 'Dave',
  },
  {
    id: 'g',
    title: 'Dave',
  },
  {
    id: 'h',
    title: 'Dave',
  },
  {
    id: 'i',
    title: 'Dave',
  },
  {
    id: 'j',
    title: 'Dave',
  },
  {
    id: 'k',
    title: 'Dave',
  },
];

export default function App() {
    return (
        <HorizontalContainer>
            <List list={data}/>
            <Map/>
        </HorizontalContainer>
    );
}
