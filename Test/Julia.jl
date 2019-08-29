#### Lagrange Interpolation Formula

using DelimitedFiles
using LinearAlgebra
using Plots; pyplot()

to = time()

function lagrange_interpolate(X,Y,t)
    C = ones(length(X))
    d = 0.0
    for i = 1:length(X)
        for j = [1:i-1;i+1:length(X)]
            C[i] = C[i]*(t-X[j])/(X[i]-X[j])
        end
        d = d + Y[i]*C[i]
    end
    return d
end

function lagrange_interpolate_plus(X,Y,t)
    idxs = eachindex(X)
    sum(Y[i] * prod((t-X[j])/(X[i]-X[j]) for j in idxs if j != i) for i in idxs)
end

A = readdlm("Data/dataSim.dat")
X = view(A,:,1)
Y = view(A,:,2)
T = 1.0:0.1:2.0
U = [lagrange_interpolate_plus(X, Y, t) for t in T]

td = time() - to
println("The time interval is $td s.")

plot(fontfamily=("Serif"),dpi=512)
# scatter!(X,Y,color="#32B432",marker=(:circle,10,Plots.stroke(:white)),label="Source")
# scatter!(T,U,color="#00B4DC",marker=(:cross,10,Plots.stroke(:white)),label="Foreast")
plot!(X,Y,color="#32B432",marker=(:circle,10,Plots.stroke(:white)),label="Source")
plot!(T,U,color="#00B4DC",marker=(:cross,10,Plots.stroke(:white)),label="Foreast")

savefig("L.pdf")

#### Richardson Extrapolation

"""
Sn = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
lim(n->∞)Sn = π^2/6 ≈ 1.6449340668482264

R1(n) = ((n+1)*S(n+1)-n*S(n))/factorial(1)
R2(n) = ((n+2)^2*S(n+1)-2*(n+1)^2*S(n+1)+n^2*S(n))/factorial(2)
……
"""

to = time()

A = readdlm("Data/Td.dat")
X = view(A,:,1)
Y = view(A,:,2)

count = length(X)

function RE1(Y)
    R1 = ones(count)
    for i in range(1; stop=count)
        if i in 1:count - 1
            R1[i] = ((i+1)*Y[i+1]-i*Y[i])/factorial(1)
        else
            R1[i] = 0
        end
        i = i + 1
    end
    return R1
end

function RE2(Y)
    R2 = ones(count)
    for i in range(1; stop=count)
        if i in 1:count - 2
            R2[i] = ((i+2)^2*Y[i+2]-2*(i+1)^2*Y[i+1]+i^2*Y[i])/factorial(2)
        else
            R2[i] = 0
        end
        i = i + 1
    end
    return R2
end

U1 = RE1(Y)
U2 = RE2(Y)

td = time() - to
println("The time interval is $td s.")

plot(fontfamily=("Serif"),dpi=512)
scatter!(X,Y, color="#B4B4B4",marker=(:circle,10,Plots.stroke(:white)),label="Source")
plot!(X[1:count-1],U1[1:count-1],color="#FF1E14",label="Foreast")
plot!(X[1:count-2],U2[1:count-2],color="#1978F0",label="Foreast")

savefig("R.pdf")