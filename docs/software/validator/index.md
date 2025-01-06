---
title: Linked Art Validator
---

## JSON Schema Validator

The [JSON schemas](/api/1.0/schema_docs/) (and also on [github](https://github.com/linked-art/json-validator)) are available as a service as well.

If your JSON records are available online without any authentication or other intervening pages or technology, then you can use this form to submit:

<form action="https://vsn673i4axyqohvvtz6g5zdpne0hxouz.lambda-url.us-east-1.on.aws/validate" method="GET">
    <b>URL</b>: <input type="text" name="url" id="url" size="120" border="1px solid black" />
<br/>
    <submit>Submit</submit>
</form>

Alternatively, if you would prefer to cut and past your JSON:

<form action="https://vsn673i4axyqohvvtz6g5zdpne0hxouz.lambda-url.us-east-1.on.aws/validate" method="POST">
    <b>JSON</b>:
    <textarea type="text" name="json" id="json" size="120" border="1px solid black" ></textarea>
<br/>
    <submit>Submit</submit>
</form>

## Other Validators

