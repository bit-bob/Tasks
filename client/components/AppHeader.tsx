import React, { ReactNode } from "react";
import styled from "styled-components";

const Container = styled.div`
  display: flex;
  padding: 50px 4px 4px 4px;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
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
