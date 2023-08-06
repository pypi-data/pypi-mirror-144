from typing import List, Tuple

import pandas as pd

# from bokeh.models.widgets.tables import NumberFormatter, StringFormatter


class PenelopeBugCheck(Exception):
    pass


def column_exists_guard(document_index: pd.DataFrame, column_name: str) -> None:
    if column_name not in document_index.columns:
        raise PenelopeBugCheck(f"expected '{column_name}' to be in {', '.join(document_index.columns)}")


def generate_temporal_ticks(categories: List[int], n_tick: int = 5) -> List[int]:
    """Gets ticks every n_tick years if category is year
    Returns all categories if all values are either, lustrum and decade"""

    if all(int(x) % 5 in (0, 5) for x in categories):
        return categories

    return list(range(low_bound(categories, n_tick), high_bound(categories, n_tick) + 1, n_tick))


def high_bound(categories: List[int], n_tick: int) -> Tuple[int, int]:
    return (lambda x: x if x % n_tick == 0 else x + (n_tick - x % n_tick))(int(max(categories)))


def low_bound(categories: List[int], n_tick: int) -> int:
    return (lambda x: x - (x % n_tick))(int(min(categories)))


# @deprecated
# def tabulator_widget(df: pd.DataFrame) -> pn.widgets.Tabulator:

#     formatters = {
#         'category': NumberFormatter(format='0'),
#         'time_period': NumberFormatter(format='0'),
#         'year': NumberFormatter(format='0'),
#         'index': StringFormatter(),
#     }

#     # def contains_filter(df, pattern, column):
#     #     if not pattern:
#     #         return df
#     #     return df[df[column].str.contains(pattern)]

#     table = pn.widgets.Tabulator(
#         df,
#         formatters=formatters,
#         layout='fit_data_table',
#         # pagination='remote',
#         # hidden_columns=['index'],
#         row_height=24,
#         show_index=False,
#     )
#     table.auto_edit = False
#     # filename, button = table.download_menu(
#     #     text_kwargs={'name': 'Enter filename', 'value': 'default.csv'},
#     #     button_kwargs={'name': 'Download table', 'width': 50}
#     # )
#     button = pn.widgets.Button(name='Export to CSV', button_type="success", width=75)
#     button.js_on_click(
#         {'table': table},
#         code="""
#     table.filename = 'table_data.csv';
#     table.download = !table.download
#     """,
#     )
#     widget = pn.Column(button, table)
#     return widget
