import React, {
  useState,
  useRef,
  useEffect,
  ComponentType,
  ReactNode,
} from "react";
import styled from "styled-components";
import TextareaAutosize from "react-textarea-autosize";

import { slate300 } from "../constants";

import { Button } from "./Button";

const Container = styled.div`
  position: relative;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  align-items: center;
  gap: 18px;
`;

const Actions = styled.div`
  position: relative;
  flex-direction: row;
  display: flex;
  gap: 5px;
`;

const InlineEditInput = styled(TextareaAutosize)`
  width: 100%;
  resize: none;
  display: block;
  height: auto;
  color: inherit;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  border: none;
  border-radius: 4px;
  background-color: ${slate300};
  padding: 7px 6px;
  &:read-only {
    cursor: text;
    &:not(:hover) {
      background: none;
    }
  }
`;

export interface InlineEditProps {
  as: ComponentType<{
    role?: string;
    onClick?: ((this: Notification, ev: Event) => any) | null;
    children: ReactNode;
  }>;
  value: string;
  onChange: (value: string) => Promise<void>;
  loading?: boolean;
}

const Heading = styled.h2`
  color: #343334;
  font-family: "Inter", sans-serif;
  font-weight: 800;
  font-size: 24px;
`;

export const InlineEdit = ({
  as: Component = Heading as any,
  value: baseValue,
  onChange,
}: InlineEditProps) => {
  const [editing, setEditing] = useState(false);
  const [value, setValue] = useState(baseValue);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (editing) {
      inputRef.current?.focus();
    }
  }, [editing]);

  useEffect(() => {
    setValue(baseValue);
  }, [baseValue]);

  return (
    <Container>
      <Component>
        <InlineEditInput
          role={!editing ? "button" : "input"}
          ref={inputRef}
          readOnly={!editing}
          value={value}
          onClick={() => {
            if (!editing) {
              setEditing(true);
            }
          }}
          onChange={(e) => {
            setValue(e.target.value);
          }}
        />
      </Component>
      {editing && (
        <Actions>
          <Button
            onClick={() => {
              setValue(baseValue);
              setEditing(false);
            }}
          >
            Cancel
          </Button>
          <Button
            variant="primary"
            onClick={async () => {
              await onChange(value);
              setEditing(false);
            }}
          >
            Accept
          </Button>
        </Actions>
      )}
    </Container>
  );
};
