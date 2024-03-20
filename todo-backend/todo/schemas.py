import graphene

from graphene_django import DjangoObjectType

from .models import Todo, User


class UserType(DjangoObjectType):
    class Meta:
        fields = ["username", "id", "first_name", "last_name"]
        # exclude = ("password",)
        model = User
        
class TodoType(DjangoObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    class Meta:
        fields = "__all__"
        model = Todo
        
class Query(graphene.ObjectType):
    todo = graphene.Field(TodoType, id=graphene.Int())
    todos = graphene.List(TodoType)
    success = graphene.Boolean()
    
    def resolve_todo(root, info, id):
                
        """
        query Todo {
            todos {
                dateTime
                id
                place
                timestamp
                title
                user(id: 10) {
                    id
                    username
                    firstName
                    lastName
                }
            }
        }
        """
        user = info.context.user
        success = True
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
        print(user)
        return user.todos.all()
    
class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    class Arguments:
        title = graphene.String()
        place = graphene.String()
        date_time = graphene.DateTime()
        
    @classmethod
    def mutate(cls, root, info, title, place, date_time):
        print(place, title, date_time)
        todo = Todo.objects.create(
            title=title,
            place=place,
            date_time=date_time,
            user=info.context.user,
        )
        
        return CreateTodo(todo)
        
        
class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        place = graphene.String()
        date_time = graphene.String()
        
    @classmethod
    def mutate(cls, root, info, title, place, date_time, id):
        todo = Todo.objects.get(id=id, user=info.context.user)
        todo.title = title
        todo.place = place
        todo.date_time = date_time
        todo.save()
        return UpdateTodo(todo)
    
class DeleteTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    success = graphene.Boolean()
    class Arguments:
        id = graphene.Int()
        
        
    @classmethod
    def mutate(cls, root, info, id):
        todo = Todo.objects.get(id=id, user=info.context.user)
        todo.delete()
        return DeleteTodo(success=True)
     
class TodoMutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    
schema = graphene.Schema(query=Query, mutation=TodoMutations)