// Selected reusable date and period utilities.
const APP_TIME_ZONE = "Asia/Shanghai";
const DAY_MS = 24 * 60 * 60 * 1000;

export type PeriodType = "day" | "week" | "month" | "year" | "range";

export type PeriodRange = {
  type: PeriodType;
  start: string;
  end: string;
  label: string;
};

export function appTimeZone() {
  return APP_TIME_ZONE;
}

export function appDateString(date = new Date()) {
  const formatter = new Intl.DateTimeFormat("en-CA", {
    timeZone: APP_TIME_ZONE,
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  });
  return formatter.format(date);
}

export function formatDateCN(dateString: string) {
  const [y, m, d] = dateString.split("-");
  return `${y}年${Number(m)}月${Number(d)}日`;
}

export function parseDateParts(dateString: string) {
  const [year, month, day] = dateString.split("-").map(Number);
  return { year, month, day };
}

function utcMs(dateString: string) {
  const { year, month, day } = parseDateParts(dateString);
  return Date.UTC(year, month - 1, day);
}

function dateFromUtcMs(ms: number) {
  return new Date(ms).toISOString().slice(0, 10);
}

export function addDays(dateString: string, days: number) {
  return dateFromUtcMs(utcMs(dateString) + days * DAY_MS);
}

export function getDayRange(dateString = appDateString()): PeriodRange {
  return { type: "day", start: dateString, end: dateString, label: formatDateCN(dateString) };
}

export function getWeekRange(dateString = appDateString()): PeriodRange {
  const { year, month, day: calendarDay } = parseDateParts(dateString);
  const day = new Date(Date.UTC(year, month - 1, calendarDay)).getUTCDay();
  const mondayOffset = day === 0 ? -6 : 1 - day;
  const start = addDays(dateString, mondayOffset);
  const end = addDays(start, 6);
  return { type: "week", start, end, label: `${formatDateCN(start)} - ${formatDateCN(end)}` };
}

export function getMonthRange(dateString = appDateString()): PeriodRange {
  const { year, month } = parseDateParts(dateString);
  const start = `${year}-${String(month).padStart(2, "0")}-01`;
  const end = dateFromUtcMs(Date.UTC(year, month, 0));
  return { type: "month", start, end, label: `${year}年${month}月` };
}

export function getYearRange(dateString = appDateString()): PeriodRange {
  const { year } = parseDateParts(dateString);
  return { type: "year", start: `${year}-01-01`, end: `${year}-12-31`, label: `${year}年` };
}

export function getLastNDaysRange(days: number, today = appDateString()): PeriodRange {
  const safeDays = Math.max(1, Math.floor(days));
  const start = addDays(today, -(safeDays - 1));
  return { type: "range", start, end: today, label: `最近${safeDays}天` };
}

export function formatPeriodCN(range: Pick<PeriodRange, "type" | "start" | "end" | "label">) {
  if (range.label) return range.label;
  if (range.type === "day") return formatDateCN(range.start);
  return `${formatDateCN(range.start)} - ${formatDateCN(range.end)}`;
}

export function isDateInRange(dateString: string, range: Pick<PeriodRange, "start" | "end">) {
  return dateString >= range.start && dateString <= range.end;
}

export function nowInAppTime() {
  return new Date().toLocaleString("zh-CN", { timeZone: APP_TIME_ZONE, hour12: false });
}
