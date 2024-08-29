from pytest_collection_issue.domain import Will, Testament


class TestDomain():
    def test_will(self):
        will = Will()
        assert will.real_property()

    def test_testament(self):
        testament = Testament()
        assert testament.personal_property()
