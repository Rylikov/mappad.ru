"""add user full name

Revision ID: 25a48fed5b8a
Revises: 2c6a2fe1dc8e
Create Date: 2019-10-26 15:19:46.492216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25a48fed5b8a'
down_revision = '2c6a2fe1dc8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_full_name'), 'users', ['full_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_full_name'), table_name='users')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###