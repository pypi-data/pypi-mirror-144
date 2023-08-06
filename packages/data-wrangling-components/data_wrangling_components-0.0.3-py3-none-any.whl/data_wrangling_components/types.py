#
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project.
#

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from dataclasses import dataclass, field


class Verb(Enum):
    Aggregate = "aggregate"
    Bin = "bin"
    Binarize = "binarize"
    Chain = "chain"
    Concat = "concat"
    Dedupe = "dedupe"
    Derive = "derive"
    Difference = "difference"
    Fetch = "fetch"
    Fill = "fill"
    Filter = "filter"
    FilterAggregateLookup = "filter-aggregate-lookup"
    Fold = "fold"
    Groupby = "groupby"
    Impute = "impute"
    Intersect = "intersect"
    Join = "join"
    Lookup = "lookup"
    MultiBinarize = "multi-binarize"
    Orderby = "orderby"
    Recode = "recode"
    Rename = "rename"
    Rollup = "rollup"
    Sample = "sample"
    Select = "select"
    Spread = "spread"
    Ungroup = "ungroup"
    Union = "union"
    Unorder = "unorder"
    Unroll = "unroll"


compound_verbs = {Verb.Chain, Verb.FilterAggregateLookup, Verb.MultiBinarize}


class Bin:
    min: Union[float, str]
    count: int


class Category:
    name: str
    count: int


@dataclass
class DataType(Enum):
    Array = "array"
    Boolean = "boolean"
    Date = "date"
    Number = "number"
    String = "string"
    Text = "text"
    Object = "object"
    Undefined = "undefined"
    Unknown = "unknown"


@dataclass
class Step:
    verb: Verb
    input: str
    output: str
    args: Dict[str, Any] = field(default_factory=dict)


@dataclass
class JoinArgs:
    other: str
    on: List[str] = field(default_factory=list)


@dataclass
class InputColumnListArgs:
    columns: List[str] = field(default_factory=list)


@dataclass
class InputColumnArgs:
    column: str


@dataclass
class OutputColumnArgs:
    to: str


@dataclass
class OutputColumnsArgs:
    to: List[str]


class FieldAggregateOperation(Enum):
    Any = "any"
    Count = "count"
    CountDistinct = "distinct"
    Valid = "valid"
    Invalid = "invalid"
    Max = "max"
    Min = "min"
    Sum = "sum"
    Product = "product"
    Mean = "mean"
    Mode = "mode"
    Median = "median"
    StDev = "stdev"
    StDevPopulation = "stdevp"
    Variance = "variance"
    ArraryAgg = "array_agg"
    ArrayAggDistinct = "array_agg_distinct"


class BinStrategy(Enum):
    Auto = "auto"
    FixedCount = "fixed count"
    FixedWidth = "fixed width"


class FilterCompareType(Enum):
    Value = "value"
    Column = "column"


class NumericComparisonOperator(Enum):
    Eq = "="
    NotEq = "!="
    Lt = "<"
    Lte = "<="
    Gt = ">"
    Gte = ">="
    NotEmpty = "is not empty"
    Empty = "is empty"


class StringComparisonOperator(Enum):
    Equal = "equals"
    NotEqual = "is not equals"
    Contains = "contains"
    StartsWith = "starts with"
    EndsWith = "ends with"
    NotEmpty = "is not empty"
    Empty = "is empty"


@dataclass
class FilterArgs(OutputColumnArgs):
    column: str
    type: FilterCompareType
    operator: Union[NumericComparisonOperator, StringComparisonOperator]
    value: Optional[Union[str, int, float, bool]] = None


class SetOp(Enum):
    Concat = "concat"
    Union = "union"
    Intersect = "intersect"
    Except = "except"


@dataclass
class SetOperationArgs:
    others: List[str]


class MathOperator(Enum):
    Add = "+"
    Subtract = "-"
    Multiply = "*"
    Divide = "/"
    Concatenate = "concat"


class SortDirection(Enum):
    Ascending = "asc"
    Descending = "desc"


@dataclass
class OrderByInstruction:
    column: str
    direction: SortDirection


@dataclass
class FillArgs(OutputColumnArgs):
    value: Union[str, int, float, bool]
