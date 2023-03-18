# Construct a narrow

A **narrow** is a set of filters for Zulip messages, that can be based
on many different factors (like sender, stream, topic, search
keywords, etc.). Narrows are used in various places in the the Zulip
API (most importantly, in the API for fetching messages).

It is simplest to explain the algorithm for encoding a search as a
narrow using a single example. Consider the following search query
(written as it would be entered in the Zulip web app's search box).
It filters for messages sent to stream `announce`, not sent by
`iago@zulip.com`, and containing the words `cool` and `sunglasses`:

```
stream:announce -sender:iago@zulip.com cool sunglasses
```

This query would be JSON-encoded for use in the Zulip API using JSON
as a list of simple objects, as follows:

```json
[
    {
        "operator": "stream",
        "operand": "announce"
    },
    {
        "operator": "sender",
        "operand": "iago@zulip.com",
        "negated": true
    },
    {
        "operator": "search",
        "operand": "cool sunglasses"
    }
]
```

The Zulip help center article on [searching for messages](/help/search-for-messages)
documents the majority of the search/narrow options supported by the
Zulip API.

Note that many narrows, including all that lack a `stream` or `streams`
operator, search the current user's personal message history. See
[searching shared history](/help/search-for-messages#searching-shared-history)
for details.

## Narrows that use IDs

The `near` and `id` operators, documented in the help center, use message
IDs for their operands.

* `near:12345`: Search messages around the message with ID `12345`.
* `id:12345`: Search for only message with ID `12345`.

There are a few additional narrow/search options (new in Zulip 2.1)
that use either stream IDs or user IDs that are not documented in the
help center because they are primarily useful to API clients:

* `stream:1234`: Search messages sent to the stream with ID `1234`.
* `sender:1234`: Search messages sent by user ID `1234`.
* `pm-with:1234`: Search the private message conversation between
  you and user ID `1234`.
* `pm-with:1234,5678`: Search the private message conversation between
  you, user ID `1234`, and user ID `5678`.
* `group-pm-with:1234`: Search all group private messages that
  include you and user ID `1234`.

The operands for these search options must be encoded either as an
integer ID or a JSON list of integer IDs. For example, to query
messages sent by a user 1234 to a PM thread with yourself, user 1234,
and user 5678, the correct JSON-encoded query is:

```json
[
    {
        "operator": "pm-with",
        "operand": [1234, 5678]
    },
    {
        "operator": "sender",
        "operand": 1234
    }
]
```
