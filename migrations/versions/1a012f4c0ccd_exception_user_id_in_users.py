"""exception user_id in users

Revision ID: 1a012f4c0ccd
Revises: fdb73f5ab466
Create Date: 2022-11-20 15:40:39.575447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a012f4c0ccd'
down_revision = 'fdb73f5ab466'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_parent', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_parent'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
