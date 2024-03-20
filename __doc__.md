# 1.1 get Todo by id
```
query Todo {
  todo(id: 1) {
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
```

# 1.2 get Todos List
```
query Todo {
  todos{
    dateTime
    id
    place
    timestamp
    title
    user {
      id
      username
      firstName
      lastName
    }
  }
}
```

# 1.3 Create Todo
```
mutation {
  createTodo(
    dateTime: "2024-03-19T10:23:56+00:00"
    place: "xyrrtgergz"
    title: "ABC"
  ) {
    todo {
      id
    }
  }
}
```

# 1.4 Update Todo
```
mutation {
  updateTodo(
    id: 1
    dateTime: "2024-03-19T10:23:56+00:00"
    place: "xyrrtgergz"
    title: "ABC"
  ) {
    todo {
      id
    }
  }
}
```

# 1.5 Delete Todo
```
mutation {
  deleteTodo(id: 10) {
    success
  }
}
```

