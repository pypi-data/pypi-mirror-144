# Injection Mold

This module provides a Spring/Micronaut-esque dependency injection system for Python using type hints.

## Example

```python
from mold import factory, singleton, inject, BeanContext

class SqlSession:
    pass

class User:
    id: str

class IUserRepo(abc.ABC):
    @abc.abstractmethod
    def get_user_by_id(self, id: str) -> User:
        raise NotImplementedError()

@singleton()
class SqlUserRepo(IUserRepo):
    def __init__(self, session: SqlSession):
        self._session = session
        
    def get_user_by_id(self, id: str) -> User:
        # ...
        pass

@factory()
def sql_session_factory() -> SqlSession:
    return SqlSession()

@inject()
def get_user_service(user_repo: IUserRepo, id: str) -> User:
    return user_repo.get_user_by_id(id)

@app.route('/user/<id>')
def get_user_route(id: str):
    user = get_user_service(id)
    return jsonify(user) 

if __name__ == '__main__':
    with BeanContext():
        app.run()
```