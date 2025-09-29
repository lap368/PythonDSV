# Concept
For certain prompts to the textgenerator Obsidian plugin, it would be useful for the user to be able to provide specific types of input beyond what can be specified via the normal context variables. The goal of this sub-project is to provide a markdown-based interface for providing such input in a reliable way.

It should be noted that the documentation of the plugin indicates that there is a way to use custom forms for input to the generator. These would be provided by the react-jsonschema-form library. However, as far as I can find, no implementation of this exists in the code base for the plugin. It may be the case that this will be implemented in the future (or that I missed it,) in which case this will become far less useful, although perhaps not entirely useless (as it allows native Obsidian input and a queue of forms.)

# Aspects of the System
## Specification of Needed Form Elements
The textgenerator template that requires a form-based input will specify aspects of the form via a set of  `form.[something]` metadata fields:

| **Field**         | **Type** | **Purpose**                                                                |
| ----------------- | -------- | -------------------------------------------------------------------------- |
| `form.fields.[x]` | Object   | Specifies details for the `x`-th field in the form. Further details below. |
### `form.fields.[x]`
This metadata field specifies the details for a specific field in the form.  It should be provided as a JSON-serializable object in the metadata, with the following fields:

| **Field**                       | **Type**                           | **Purpose**                                                                                                | Notes                                                                                                                    |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `form.fields.[x].identifier`    | String                             | Specifies the identifier that this field will be referred to this field's response in the resulting object | --                                                                                                                       |
| `form.fields.[x].title`         | String                             | Specifies the text that will appear to prompt for this field (e.g. "username" or "Desired tone.")          | Defaults to the value provided in `identifier` if not provided.                                                          |
| `form.fields.[x].required`      | Boolean                            | Specifies whether this field is required                                                                   | --                                                                                                                       |
| `form.fields.[x].type`          | "multiple_choice" \| "open_answer" | Specifies the type of question                                                                             | --                                                                                                                       |
| `form.fields.[x].options`       | Array of Strings                   | Specifies the available options                                                                            | Only available if `form.fields.[x].type == "multiple_choice"`. Required if so.                                           |
| `form.fields.[x].min_num_picks` | Integer                            | Specifies the minimum number of options that can be selected                                               | Only available if `form.fields.[x].type == "multiple_choice"`. Defaults to 1 if not provided.                            |
| `form.fields.[x].max_num_picks` | Integer                            | Specifies the maximum number of options that can be selected                                               | Only available if `form.fields.[x].type == "multiple_choice"`. Defaults to the value in `min_num_picks` if not provided. |

## 