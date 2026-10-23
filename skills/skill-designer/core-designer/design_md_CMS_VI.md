# Design.md

> Ngôn ngữ tài liệu: Tiếng Việt
> 
> Toàn bộ guideline, component documentation, design token và developer handoff nên được viết và maintain bằng tiếng Việt để đồng nhất giữa team Design, Product và Frontend.

# Untitled UI – PRO VARIABLES (v5.0)

## Overview

This document describes the visual language, token architecture, component philosophy, and UI standards derived from the Untitled UI PRO VARIABLES design system.

Untitled UI is a modern, scalable, enterprise-grade UI framework designed for SaaS products, dashboards, admin systems, and web applications.

---

# 1. Design Philosophy

## Core Principles

### Clarity First
Interfaces should communicate hierarchy and intent immediately.

### Scalable Systems
Every style should be tokenized and reusable.

### Accessibility by Default
Readable typography, contrast-safe colors, and keyboard accessibility are required.

### Minimal but Expressive
Use restrained visuals with intentional emphasis.

---

# 2. Visual Style

## Overall Direction
- Minimal modern SaaS aesthetic
- High whitespace usage
- Soft neutral surfaces
- Subtle shadows and borders
- Rounded corners
- Structured typography hierarchy
- Component-first architecture

## Design Characteristics
- Enterprise-ready UI
- Product-focused layouts
- Clean dashboard patterns
- Token-driven consistency

---

# 3. Token Architecture

## Token Categories

### Color Tokens
```txt
Color / Primary / 500
Color / Gray / 100
Color / Error / 600
```

### Spacing Tokens
```txt
Spacing / 1
Spacing / 2
Spacing / 4
```

### Radius Tokens
```txt
Radius / sm
Radius / md
Radius / xl
```

### Shadow Tokens
```txt
Shadow / xs
Shadow / md
Shadow / xl
```

### Typography Tokens
```txt
Text / md / Regular
Display / lg / Semibold
```

---

# 4. Color System

## Primary Palette
The primary brand color for the system is:

```txt
#4564ED
```

This color is used for:
- Primary buttons
- Active navigation
- Links
- Focus states
- Key interaction highlights
- Charts and data emphasis

## Recommended Primary Scale
| Token | Value |
|---|---|
| Primary / 50 | #EEF2FF |
| Primary / 100 | #DCE4FF |
| Primary / 200 | #BCCAFF |
| Primary / 300 | #93A8FF |
| Primary / 400 | #6F86FF |
| Primary / 500 | #4564ED |
| Primary / 600 | #3451D4 |
| Primary / 700 | #2740B5 |
| Primary / 800 | #1E318E |
| Primary / 900 | #17266B |

## Primary Usage Rules
- Use `Primary / 500` as the default brand color.
- Use darker shades for hover and active states.
- Use lighter shades for backgrounds and focus rings.
- Avoid using the primary color excessively in large surfaces.

## Neutral Palette
Neutral gray scales are used extensively for:
- Typography
- Borders
- Background surfaces
- Data-heavy interfaces

## Semantic Colors
| Semantic | Usage |
|---|---|
| Success | Positive feedback |
| Warning | Attention states |
| Error | Validation and destructive actions |
| Info | Informational messaging |

## Color Usage Rules
- Use semantic colors consistently.
- Prefer neutral backgrounds.
- Avoid oversaturated compositions.
- Use color hierarchy intentionally.

---

# 5. Typography System

## Font Philosophy
Typography is designed for:
- Dense information readability
- Dashboard clarity
- Strong hierarchy
- Accessibility

## Recommended Font
- Inter

## Display Scale
| Token | Size | Weight |
|---|---|---|
| Display 2XL | 72px | Bold |
| Display XL | 60px | Bold |
| Display LG | 48px | Semibold |
| Display MD | 36px | Semibold |
| Display SM | 30px | Semibold |

## Text Scale
| Token | Size | Weight |
|---|---|---|
| Text XL | 20px | Medium |
| Text LG | 18px | Medium |
| Text MD | 16px | Regular |
| Text SM | 14px | Regular |
| Text XS | 12px | Medium |

## Typography Rules
- Maintain vertical rhythm.
- Use limited font weights.
- Avoid long paragraphs.
- Prefer semantic hierarchy.

---

# 6. Spacing System

## Base Unit
The system follows a 4px / 8px spacing rhythm.

## Spacing Scale
| Token | Value |
|---|---|
| 0.5 | 2px |
| 1 | 4px |
| 1.5 | 6px |
| 2 | 8px |
| 3 | 12px |
| 4 | 16px |
| 5 | 20px |
| 6 | 24px |
| 8 | 32px |
| 10 | 40px |
| 12 | 48px |
| 16 | 64px |

## Guidelines
- Use consistent padding.
- Maintain predictable layout rhythm.
- Avoid arbitrary spacing values.

---

# 7. Radius System

| Token | Value |
|---|---|
| radius-xs | 4px |
| radius-sm | 6px |
| radius-md | 8px |
| radius-lg | 12px |
| radius-xl | 16px |
| radius-2xl | 24px |
| radius-full | 9999px |

## Usage
- Buttons: md
- Cards: lg
- Modals: xl
- Pills/Badges: full

---

# 8. Shadows & Elevation

## Shadow Philosophy
Shadows are subtle and layered.

## Shadow Levels
| Token | Usage |
|---|---|
| xs | Inputs |
| sm | Small cards |
| md | Dropdowns |
| lg | Floating surfaces |
| xl | Modals |

## Guidelines
- Avoid harsh shadows.
- Combine borders with subtle elevation.
- Use elevation to communicate hierarchy.

---

# 9. Layout System

## Desktop Grid
- 12-column layout
- Large content gutters
- Flexible container widths

## Tablet Grid
- 8-column layout

## Mobile Grid
- 4-column layout

## Layout Principles
- Use modular content sections.
- Prioritize readability over density.
- Maintain strong alignment.

---

# 10. Components

# Buttons

## Variants
- Primary
- Secondary
- Tertiary
- Link
- Destructive

## Sizes
- xs
- sm
- md
- lg
- xl

## States
- Default
- Hover
- Focus
- Disabled
- Loading

## Guidelines
- Only one primary CTA per section.
- Use tertiary for low-emphasis actions.

---

# Inputs

## Supported Components
- Text field
- Search input
- Select
- Textarea
- Date picker
- Checkbox
- Radio
- Toggle

## Rules
- Always include labels.
- Show helper text when necessary.
- Surface validation errors clearly.

---

# Badges

## Usage
- Status indicators
- Labels
- Metadata

## Variants
- Gray
- Brand
- Success
- Warning
- Error

---

# Tables

## Principles
- Readability first
- Clear row separation
- Sticky headers when needed
- Responsive overflow handling

---

# Cards

## Anatomy
- Header
- Supporting text
- Content
- Actions

## Usage
- Metrics
- Dashboards
- Content previews
- Settings panels

---

# Navigation

## Navigation Types
- Sidebar navigation
- Top navigation
- Breadcrumbs
- Pagination
- Tabs

## Navigation Rules
- Maintain predictable location.
- Highlight active states clearly.
- Support keyboard navigation.

---

# 11. Data Visualization

## Chart Style
- Minimal visual clutter
- Neutral backgrounds
- Accessible color differentiation

## Recommended Charts
- Area chart
- Line chart
- Bar chart
- Donut chart
- KPI widgets

---

# 12. Motion & Interaction

## Motion Principles
- Fast
- Smooth
- Purposeful
- Non-distracting

## Duration Recommendations
| Interaction | Duration |
|---|---|
| Hover | 150ms |
| Dropdown | 200ms |
| Modal | 250ms |
| Page transition | 300ms |

## Easing
Prefer ease-out motion curves.

---

# 13. Accessibility

## Requirements
- WCAG AA compliance
- Keyboard accessibility
- Visible focus indicators
- Proper semantic HTML

## Color Accessibility
- Avoid low-contrast text.
- Never rely solely on color.

## Typography Accessibility
- Minimum body text: 14px
- Recommended body text: 16px

---

# 14. Responsive Design

## Breakpoints
| Device | Width |
|---|---|
| Mobile | <768px |
| Tablet | 768px–1024px |
| Desktop | 1024px–1440px |
| Large Desktop | 1440px–1920px |
| Wide Screen / Full HD | ≥1920px |

## 1920px Desktop Strategy

For 1920px and larger screens, the layout should not simply stretch all content across the full viewport width.

### Recommended Behavior
- Use a max-content container width.
- Maintain readable line lengths.
- Increase whitespace proportionally.
- Preserve component density consistency.
- Allow dashboards to expand using modular grid areas.

## Recommended Max Widths
| Layout Type | Max Width |
|---|---|
| Standard Content | 1280px–1440px |
| Dashboard Layout | 1600px–1720px |
| Data-Heavy Workspace | 1800px |

## Wide Screen Rules
- Avoid ultra-wide text blocks.
- Keep sidebar widths fixed.
- Use adaptive grid columns.
- Increase gutters and spacing carefully.
- Expand analytics widgets horizontally when appropriate.

## Example 1920px Layout Structure
```txt
[Sidebar 280px] [Main Content 1440px–1600px] [Optional Utility Panel]
```

## Responsive Rules
- Collapse navigation on mobile.
- Stack dashboard cards vertically on smaller screens.
- Preserve dashboard readability on ultra-wide displays.
- Prevent excessive empty space.
- Use max-width containers for content-focused pages.

---|---|
| Mobile | <768px |
| Tablet | 768px–1024px |
| Desktop | >1024px |
| Wide | >1440px |

## Responsive Rules
- Collapse navigation on mobile.
- Stack dashboard cards vertically.
- Reduce table complexity on small screens.

---

# 15. Dark Mode Strategy

## Principles
- Preserve contrast hierarchy.
- Reduce eye strain.
- Maintain semantic consistency.

## Dark Surfaces
Use layered neutral backgrounds instead of pure black.

---

# 16. Naming Conventions

## Component Naming
```txt
Component / Variant / Size / State
```

Example:
```txt
Button / Primary / MD / Hover
```

## Token Naming
```txt
Category / Property / Scale
```

Example:
```txt
Color / Gray / 700
```

---

# 17. Developer Handoff

## Recommended Frontend Stack
- Tailwind CSS
- CSS Variables
- Storybook
- Design Tokens pipeline

## Implementation Rules
- Avoid hardcoded values.
- Use token references.
- Centralize variants.
- Maintain accessibility parity.

## Example Token Structure

```json
{
  "colors": {
    "primary": {
      "500": "#6941C6"
    }
  }
}
```

---

# 18. Documentation Standards

Each component should document:
- Anatomy
- Variants
- States
- Accessibility
- Responsive behavior
- Usage examples
- Do/Don't examples

---

# 19. Recommended Engineering Workflow

## Design → Dev Flow
1. Create tokenized design primitives
2. Build reusable components
3. Connect tokens to frontend theme
4. Document in Storybook
5. Validate accessibility
6. Ship incrementally

---

# 20. Future Extensions

Potential future additions:
- RTL support
- Localization support
- Multi-theme architecture
- Advanced motion tokens
- AI-assisted UI patterns
- Adaptive dashboards

---

# Conclusion

Untitled UI PRO VARIABLES provides a scalable and production-ready foundation for enterprise SaaS interfaces. The system emphasizes clarity, consistency, accessibility, and token-driven scalability to support modern product teams.

