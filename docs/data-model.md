# Модель данных

Стек: Django (Python) + SQLite. Модели описаны в коде:
`MCIKIT/users/models.py`, `MCIKIT/add_event/models.py`;
ER-диаграмма: [docs/data/ER.png](data/ER.png).

## Сущности и поля

### User (`users.User`, наследник `AbstractUser`)
| Поле | Тип | Описание |
|---|---|---|
| Name_User | CharField(30) | ФИО |
| VK_id | CharField(30) | ВК ID |
| Number_of_group | CharField(30) | Номер группы |
| Number_of_events_attended | Integer, default 0 | Посещённых мероприятий |
| Avatar | ImageField, null | Аватар |
| role | CharField: `user` / `pro_user` / `super_user` | Роль, по умолчанию `user` |

### Event (`add_event.Event`)
| Поле | Тип | Описание |
|---|---|---|
| title_event | Text | Название |
| description_Event | Text | Описание |
| event_place | Text | Место проведения |
| event_date / event_time | Date / Time (по умолчанию 12:00) | Дата и время начала |
| Event_photo | ImageField | Афиша |
| max_members | PositiveInteger, default 0 | Макс. участников |
| registration_closed | Boolean | Регистрация закрыта |
| users_members | M2M → User | Зарегистрированные участники |
| organizers | M2M → User через EventOrganizer | Организаторы |

### EventOrganizer (`users.EventOrganizer`)
`user` → User, `event` → Event, `added_by` → User (SET_NULL), `date_added`. Уникальность пары (user, event).

### EventRating (`add_event.EventRating`)
`user`, `event`, `rating` (1–5), `likes`, `dislikes`, `timestamp`. Уникальность пары (user, event).

### ExtraInfo (`add_event.ExtraInfo`) — доп. вопрос к регистрации
`event` → Event, `question`, `field_type` (`text` / `choice` / `team`), `allow_multiple`, `min_team_size`, `max_team_size`.

### Choice (`add_event.Choice`)
`extra_info` → ExtraInfo, `value` — вариант ответа.

### UserAnswer (`add_event.UserAnswer`)
`user`, `extra_info`, `answer`, `is_team_captain`, `team_name`, `team_members` (M2M → User).
