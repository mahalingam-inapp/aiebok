# A chatbot answer that changed a travel decision

## What happened

After the death of their grandmother in 2022, Jake Moffatt needed to book flights. Air Canada’s website chatbot indicated that they could apply for a bereavement fare after purchasing the tickets. A linked policy page described a different procedure. Moffatt booked and later learned the airline would not apply the fare retroactively. In 2024, the British Columbia Civil Resolution Tribunal found that reliance on the chatbot was reasonable in this instance and awarded damages. The decision gives no implementation details about the chatbot. [Civil Resolution Tribunal decision, paragraphs 13–30](https://longangz.com/ai/case-documents/canada-moffatt-air-canada/source-1.pdf)

## At the design review

A link can help a traveler inspect an answer. It cannot make a contradictory instruction reliable, particularly when the wording suggests they can act now and check later. Separate **finding the current policy** from **making a claim about the policy**. Even if the right document reaches the assistant, the answer can still misstate when the policy applies.

Put yourself in charge of a fictional ticket assistant. The current fare document says the customer must contact staff *before purchase*. An older help article says they may submit a request *after purchase*. The traveler asks, “Can I buy now and claim the discount later?”

| Decision | Evidence for the release test |
|---|---|
| Determine which source controls | The current policy has an effective date and a named owner. The older article is marked superseded. |
| Validate the practical instruction | The output preserves the ‘before purchase’ condition and cites the relevant passage. |
| Handle a genuine conflict | If the controlling source cannot be established, the service offers a support handoff before the user is asked to buy. |

Before reading on, draft the exact two sentences you would send. Can the traveler tell what they should do next? Would you make the same choice if the policy had a recently added exception?

[AI Literacy](../courses/ai-literacy/index.md) · [Knowledge and Retrieval Systems](../books/06-knowledge-and-retrieval-systems/index.md) · [Casebook](index.md)
