import { render } from "@testing-library/react";
import { describe, expect, test } from "vitest";
import App from "../App";

describe("true test", () => {
    test("true test", () => {
        render(<App />)
        expect(true).toBe(true)
    })
})