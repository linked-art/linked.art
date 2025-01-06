---
title: Linked Art Validator
---

## JSON Schema Validator

The [JSON schemas](/api/1.0/schema_docs/) (and also on [github](https://github.com/linked-art/json-validator)) are available as a service as well.

If your JSON records are available online without any authentication or other intervening pages or technology, then you can use this form to submit:

<form action="https://vsn673i4axyqohvvtz6g5zdpne0hxouz.lambda-url.us-east-1.on.aws/validate" method="GET">
    <b>URL</b>:
    <br/>
    <input type="text" name="url" id="url" size="120" style="border: 1px solid black" />
    <br/>
    <input type="submit" name="validate"></input>
</form>

<hr/>

Alternatively, if you would prefer to cut and paste your JSON:

<form action="https://vsn673i4axyqohvvtz6g5zdpne0hxouz.lambda-url.us-east-1.on.aws/validate" method="POST">
    <b>JSON</b>:
    <br/>
    <textarea type="text" name="json" id="json" cols="120" rows="10" style="border: 1px solid black" ></textarea>
    <br/>
    <input type="submit" name="validate"></input>
</form>

## Other Validators

Other validators are in the works, including one based on SHACL.

