import React from "react";
import styled from "styled-components";

const Button = styled.button`
  display: flex;
  padding: 10px;
  justify-content: center;
  align-items: center;
  gap: 10px;

  border-radius: 8px;
  border: none;
  background-color: #BE123C;

  transition: all 100ms ease-in-out;
  &:hover {
    background-color: #C71440;
  }
  &:active {
    transform: scale(0.95);
  }

  color: #FFF;
  text-align: center;

  /* Body */
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  letter-spacing: -0.333px;
`;

export interface DeleteButtonProps {
  onDelete?: () => void;
}

export const DeleteButton = ({ onDelete }: DeleteButtonProps) => {
  return (
    <Button onClick={onDelete}>
      Delete
    </Button>
  );
};
