import test from "node:test";
import assert from "node:assert/strict";
import {
  addDays, getWeekRange, getMonthRange,
  getYearRange, getLastNDaysRange, isDateInRange,
} from "../samples/study-logs/period.ts";

test("year boundary and leap day arithmetic", () => {
  assert.equal(addDays("2025-12-31", 1), "2026-01-01");
  assert.equal(addDays("2024-02-28", 1), "2024-02-29");
  assert.equal(addDays("2024-02-29", 1), "2024-03-01");
});

test("weeks start Monday, including Sunday transitions", () => {
  assert.equal(getWeekRange("2026-10-26").start, "2026-10-26");
  assert.equal(getWeekRange("2026-10-26").end, "2026-11-01");
  assert.equal(getWeekRange("2026-11-01").start, "2026-10-26");
});

test("natural month, year and rolling-range rules", () => {
  assert.equal(getMonthRange("2024-02-15").end, "2024-02-29");
  assert.equal(getMonthRange("2026-12-15").end, "2026-12-31");
  assert.equal(getYearRange("2026-10-26").start, "2026-01-01");
  assert.equal(getLastNDaysRange(7, "2026-03-01").start, "2026-02-23");
  assert.equal(getLastNDaysRange(7, "2026-03-01").end, "2026-03-01");
});

test("a period includes both boundaries", () => {
  const range = getWeekRange("2026-10-26");
  assert.equal(isDateInRange("2026-10-26", range), true);
  assert.equal(isDateInRange("2026-11-01", range), true);
  assert.equal(isDateInRange("2026-11-02", range), false);
});
