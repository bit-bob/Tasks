import { formatElapsedTime } from "./elapsedTime";

test("expect 40 seconds to be formatted as '00:40'", () => {
  expect(formatElapsedTime(40)).toEqual("00:40");
});
