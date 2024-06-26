import numpy as np
import torch
from prtm.models.openfold.model.embedders import (
    InputEmbedder,
    RecyclingEmbedder,
    TemplateAngleEmbedder,
    TemplatePairEmbedder,
)


def test_shape():
    tf_dim = 2
    msa_dim = 3
    c_z = 5
    c_m = 7
    relpos_k = 11

    b = 13
    n_res = 17
    n_clust = 19

    tf = torch.rand((b, n_res, tf_dim))
    ri = torch.rand((b, n_res))
    msa = torch.rand((b, n_clust, n_res, msa_dim))

    ie = InputEmbedder(tf_dim, msa_dim, c_z, c_m, relpos_k)

    msa_emb, pair_emb = ie(tf, ri, msa)
    assert msa_emb.shape == (b, n_clust, n_res, c_m)
    assert pair_emb.shape == (b, n_res, n_res, c_z)


def test_shape():
    batch_size = 2
    n = 3
    c_z = 5
    c_m = 7
    min_bin = 0
    max_bin = 10
    no_bins = 9

    re = RecyclingEmbedder(c_m, c_z, min_bin, max_bin, no_bins)

    m_1 = torch.rand((batch_size, n, c_m))
    z = torch.rand((batch_size, n, n, c_z))
    x = torch.rand((batch_size, n, 3))

    m_1, z = re(m_1, z, x)

    assert z.shape == (batch_size, n, n, c_z)
    assert m_1.shape == (batch_size, n, c_m)


def test_shape():
    template_angle_dim = 51
    c_m = 256
    batch_size = 4
    n_templ = 4
    n_res = 256

    tae = TemplateAngleEmbedder(
        template_angle_dim,
        c_m,
    )

    x = torch.rand((batch_size, n_templ, n_res, template_angle_dim))
    x = tae(x)

    assert x.shape == (batch_size, n_templ, n_res, c_m)


def test_shape():
    batch_size = 2
    n_templ = 3
    n_res = 5
    template_pair_dim = 7
    c_t = 11

    tpe = TemplatePairEmbedder(
        template_pair_dim,
        c_t,
    )

    x = torch.rand((batch_size, n_templ, n_res, n_res, template_pair_dim))
    x = tpe(x)

    assert x.shape == (batch_size, n_templ, n_res, n_res, c_t)
