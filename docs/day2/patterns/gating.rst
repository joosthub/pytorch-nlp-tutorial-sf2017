Gating
======



.. code-block:: python


    resetgate = F.sigmoid(i_r + h_r)
    inputgate = F.sigmoid(i_i + h_i)
    newgate = F.tanh(i_n + resetgate * h_n)
    hy = newgate + inputgate * (hidden - newgate)
