# SEsocial

A python repository for verifying and generating swedish social security numbers.

## Installation

### Easy:

`pip install SE-social`

### Advanced:

`git clone http://github.com/WaldemarBjornstrom/SEsocial.git`

Then go to the SEsocial directory you just downloaded and copy the sesocial folder into your project.

## Usage

```python
import sesocial

sesocial.verify('yymmddxxxx') # Returns True or False

sesocial.gender('yymmddxxxx') # Returns Male or Female

sesocial.generate() # Returns format yymmddxxxx

```

OPTIONAL: You can add age and gender to `sesocial.generate(age, gender)`

Note: You could also  `import sesocial as a` or swap out a to anyting you like.
And then use the commands like `a.verify('yymmddxxxx')`

## License

This project lies under the MIT License. See [LICENSE](LICENSE "LICENSE")
