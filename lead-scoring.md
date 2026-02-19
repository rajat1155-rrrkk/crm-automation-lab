# Lead Scoring Engine

This module simulates enterprise-style CRM lead scoring logic.

## Purpose

Implements weighted scoring based on:
- Industry segment
- Company size
- Engagement score

## Scoring Logic

| Factor            | Weight |
|------------------|--------|
| High-value industry | +30   |
| Company size > 500  | +25   |
| Company size > 100  | +15   |
| Engagement score    | Max 40 |

## Design Considerations

- Modular structure for extensibility
- Clear separation of scoring logic
- Designed to simulate CRM automation workflows
