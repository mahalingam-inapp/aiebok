# Reading Progress

AIEBOK includes a **browser-local progress bar** at the top of every page. It helps you see how far you are through the reading curriculum and pick up where you left off.

## What it tracks

<!-- site-stats:progress:start -->
| Track | Items |
|---|---:|
| Start here | 3 onboarding pages |
| Guided books | 78 chapters |

**Total:** 81 reading checkpoints. **Labs are not tracked** — run them in the repo at your own pace.
<!-- site-stats:progress:end -->

## How progress is saved

Progress is stored **only on your device**:

- **localStorage** — full progress state
- **Cookies** — backup of completed IDs and last page (`aiebok_done`, `aiebok_last`, 1-year lifetime)

Nothing is sent to a server. There are no accounts. Clearing site data in your browser removes progress.

!!! tip "Return anytime"
    Open the site on the same browser — the bar shows your percentage and a **Continue** link to the next unread chapter.

## How items get marked complete

1. **Automatically** — after ~6 seconds on a tracked page.
2. **Manually** — use **Mark chapter complete** at the bottom of a chapter, or open **Details** on the progress bar.

## Reset

Open **Details** on the progress bar → **Reset all progress**.

## Privacy

No backend, no cross-device sync, no analytics requirement — progress stays on your machine.

See also: [Newcomer guide](../getting-started/newcomer-guide.md) · [Hands-on start](../labs/start-here.md)
