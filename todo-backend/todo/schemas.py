import graphene

from graphene_django import DjangoObjectType

from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        fields = "__all__"
        model = Todo
        
class Query(graphene.ObjectType):
    todo = graphene.Field(TodoType, id=graphene.Int())
    todos = graphene.List(TodoType)
    
    def resolve_todo(root, info, id):
                
        """
        query Todo {
            todo(id:1) {
                dateTime
                id
                place
                timestamp
                title
            }
        }
        """
        user = info.context.user
        return Todo.objects.select_related("user").get(id=id, user=user)
 
    def resolve_todos(root, info):
        
        """
        query Todos {
            todos {
                dateTime
                id
                place
                timestamp
                title
            }
        }
        """
        user = info.context.user
        # print(user)
        return user.todos.all()
 
schema = graphene.Schema(query=Query)