import justpy as jp
from typing import Awaitable, Callable, Dict, List, Optional, Union
from .choice_element import ChoiceElement

class Radio(ChoiceElement):

    def __init__(self,
                 options: Union[List, Dict],
                 *,
                 value: any = None,
                 on_change: Optional[Union[Callable, Awaitable]] = None,
                 ):
        """Radio Selection Element

        :param options: a list ['value1', ...] or dictionary `{'value1':'label1', ...}` specifying the options
        :param value: the inital value
        :param on_change: callback to execute when selection changes
        """
        view = jp.QOptionGroup(options=options, input=self.handle_change, temp=False)

        super().__init__(view, options, value=value, on_change=on_change)
