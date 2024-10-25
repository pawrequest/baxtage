from sqlmodel import Field, SQLModel


class ActShowLink(SQLModel, table=True):
    act_id: int | None = Field(default=None, foreign_key='act.id', primary_key=True)
    show_id: int | None = Field(default=None, foreign_key='show.id', primary_key=True)


class ActArtistLink(SQLModel, table=True):
    act_id: int | None = Field(default=None, foreign_key='act.id', primary_key=True)
    artist_id: int | None = Field(default=None, foreign_key='artist.id', primary_key=True)


