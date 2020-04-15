"""tracks table

Revision ID: 2c6a2fe1dc8e
Revises: b13f9c71d65f
Create Date: 2019-10-11 17:43:25.530401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6a2fe1dc8e'
down_revision = 'b13f9c71d65f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracks', sa.Column('description', sa.String(length=250), nullable=True))
    op.add_column('tracks', sa.Column('raw_gpx', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tracks', 'raw_gpx')
    op.drop_column('tracks', 'description')
    # ### end Alembic commands ###
