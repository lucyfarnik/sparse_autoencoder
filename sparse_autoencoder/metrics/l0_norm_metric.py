"""L0 (sparsity) norm metric."""
from collections import OrderedDict
from typing import final

import torch

from sparse_autoencoder.metrics.train.abstract_train_metric import (
    AbstractTrainMetric,
    TrainMetricData,
)


@final
class L0NormMetric(AbstractTrainMetric):
    """L0 (sparsity) norm metric."""

    @final
    def calculate(self, data: TrainMetricData) -> OrderedDict[str, float]:
        """Create a log item for Weights and Biases."""
        # The L0 norm is the number of non-zero elements
        # (We're averaging over the batch)
        acts = data.learned_activations
        value = (torch.sum(acts != 0) / acts.size(0)).item()
        return OrderedDict(l0_norm=value)
