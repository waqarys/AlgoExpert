from speclib import *
TITLE = "MLExpert · Singular Value Decomposition"; OUT = "mlexpert/15_svd"; M = "mlexpert/mlexpert/svd.py"
SLIDES = [
 title("Singular Value Decomposition", "Truncated SVD by power iteration", "The singular value decomposition underpins PCA, recommenders, and compression. Here we build a truncated SVD from scratch using power iteration and deflation."),
 bullets("The problem", ["Large matrix A (users × items, documents × words)", "Want its best rank-k approximation", "Without a full, expensive decomposition"],
  "We have a big matrix, like users by items, and want its best low-rank approximation, keeping only the top k patterns, without paying for a full decomposition."),
 eqs("SVD", [r"$A=U\Sigma V^\top=\sum_i \sigma_i\,u_i v_i^\top$"], ["σ₁ ≥ σ₂ ≥ … ≥ 0", "Top-k terms = best rank-k approximation (Eckart–Young)"],
  "Any matrix is a sum of rank-one pieces, each a singular value times an outer product of left and right singular vectors. Keeping the k largest terms gives the best rank-k approximation, a result known as Eckart-Young."),
 bullets("Power iteration", ["Start with a random unit vector v", "Repeat: v ← AᵀA v, normalise", "v converges to the top right singular vector", "σ = ‖Av‖, u = Av / σ"],
  "To find the top piece, use power iteration. Multiply a random vector by A transpose A and normalise, again and again. The component along the dominant direction grows fastest, so v converges to the top right singular vector. Then sigma is the length of A v, and u is A v divided by sigma."),
 bullets("Deflation", ["Subtract the found piece: R ← R − σ u vᵀ", "Repeat power iteration on R for the next one", "k rounds → k components"],
  "To get the next component, deflate: subtract the found rank-one piece from the matrix, and run power iteration again on what's left. After k rounds we have the top k singular triples."),
 code("truncated_svd", src(M, "truncated_svd"), "Here's the full function. For each of k components: random start, iterate with A transpose A on the residual, compute sigma and u, store them, and deflate."),
 bullets("Complexity & trade-offs", ["O(k · iters · n · d), cheap for small k", "Slow if σ_k ≈ σ_{k+1} (small spectral gap)", "Errors accumulate through deflation", "Production: randomized SVD, Lanczos"],
  "Cost is k times iterations times the matrix size, great when k is small. Convergence slows when consecutive singular values are close, and small errors accumulate through deflation. In production, randomized SVD or Lanczos methods are the standard."),
 bullets("Recap", ["A = sum of σ u vᵀ pieces", "Power iteration finds the top piece", "Deflate and repeat", "Basis for PCA, LSA, recommenders"],
  "To recap: SVD writes a matrix as a sum of ranked pieces. Power iteration finds the top one, deflation exposes the next, and this is the engine behind PCA, latent semantic analysis, and recommenders."),
]
