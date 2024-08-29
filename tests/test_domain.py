from pytest_collection_issue.domain import Will, Testament as _Testament


class TestDomain():
    def test_will(self):
        will = Will()
        assert will.real_property()

    def test_testament(self):
        testament = _Testament()
        assert testament.personal_property()
