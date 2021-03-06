"""empty message

Revision ID: 37c604802df6
Revises: 
Create Date: 2018-08-27 12:15:23.944455

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '37c604802df6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pallet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('bin_', sa.String(length=60), nullable=True),
    sa.Column('item_', sa.String(length=10), nullable=True),
    sa.Column('lot_id', sa.String(length=60), nullable=True),
    sa.Column('num_of_pieces', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['bin_'], ['bin.name'], ),
    sa.ForeignKeyConstraint(['item_'], ['item.item_code'], ),
    sa.ForeignKeyConstraint(['lot_id'], ['lot.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('bins')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bins',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('location_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name='bins_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('pallet')
    op.drop_table('bin')
    # ### end Alembic commands ###
