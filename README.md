Demonstrates a problem with pytest that I can't figure out.

There is a test class, TestDomain, in the tests folder that is correctly
automatically detected. There is a domain class, Testament, in the source
folder, that causes a warning:

```
src/pytest_collection_issue/domain.py:6
  src/pytest_collection_issue/domain.py:6: PytestCollectionWarning: cannot collect test class 'Testament' because it has a __init__ constructor (from: tests/test_domain.py)
    class Testament(object):
```

After many Google searches, I have tried a variety of things to get pytest
to ignore things found in `src`. I understand that I could tag each object
starting with `Test` with `__test__ = False`, but in my real project there
will be a lot of those. I'd like to find some way to tell pytest once that
it should never treat anything in the `src` directory as a test. Or,
equivalently, to tell it only look in `tests`.