class IssueSerializer < ActiveModel::Serializer
    attributes :id ,:project , :tag
    has_many :users
end
