import React, {
  useState,
  useRef,
  useEffect,
  ComponentType,
  ReactNode,
} from "react";
import styled from "styled-components";
import TextareaAutosize from "react-textarea-autosize";

import { Button } from "./Button";

const Container = styled.div`
  position: relative;
`;

const Actions = styled.div`
  position: absolute;
  right: 0;
  top: 0;
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
  padding: 6px;
  margin: 4px 6px 10px -6px;
  border-radius: 4px;
  background-color: #d6d5d9;
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
  margin: 8px 0 14px 0;
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
