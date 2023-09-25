import React, { ReactNode } from "react";
import styled from "styled-components";
import { transparentize } from "polished";

import { slate50, slate950 } from "../constants";

const Container = styled.div`
  display: flex;
  padding: 50px 18px 12px 8px;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;

  // pin the heading to the top of the screen
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  background-color: ${slate50};

  // make the total height of the header 100px
  // to make the padding on the rest of the app a round number
  height: 38px;

  // add a shadow underneath
  box-shadow: 0px 4px 36px 0px ${transparentize(0.9, slate950)},
    0px 1px 4px 0px ${transparentize(0.9, slate950)};
`;

const Actions = styled.div`
  display: flex;
`;

export const AppHeaderTitle = styled.h1`
  color: #000;
  text-align: center;
  /* Title */
  font-family: Comfortaa;
  font-size: 32px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  letter-spacing: -0.333px;
  text-transform: capitalize;
`;

export interface AppHeaderProps {
  title: ReactNode;
  actions?: ReactNode;
}

export const AppHeader = ({ title, actions }: AppHeaderProps) => {
  return (
    <Container>
      <AppHeaderTitle>{title}</AppHeaderTitle>
      <Actions>{actions}</Actions>
    </Container>
  );
};
