#include <benchmark/benchmark.h>
#include <algorithm>
#include <array>
#include <iostream>
#include <list>
#include <random>
#include <string>
#include <vector>

template <int Words>
struct Node
{
    std::array<int, Words> data{};
    auto operator=(int i) -> Node&
    {
        for (auto& x : data) { x = i++; }
        return *this;
    }
    auto operator<(Node n) -> bool { return data[0] < n.data[0]; }
};

template <typename C>
static auto gen_random_data(int size) -> C
{
    auto r = std::random_device{};
    auto e = std::default_random_engine{r()};
    auto uniform_dist = std::uniform_int_distribution<int>{};
    auto return_container = C(size);
    for (auto& x : return_container) { x = uniform_dist(e); }
    return return_container;
}

template <typename C>
static auto copy_sort(const C& container) -> C
{
    auto copy = C{};
    for (auto x : container)
    {
        auto it = copy.begin();
        for (; it != copy.end() and *it < x; ++it) {}
        copy.insert(it, x);
    }
    return copy;
}

template <int NodeSize>
static void BM_vector_insert(benchmark::State& state)
{
    auto random_vector = gen_random_data<std::vector<Node<NodeSize>>>(state.range(0));
    for (auto _ : state)
    {
        auto copy = std::vector<Node<NodeSize>>{};
        benchmark::DoNotOptimize(copy = copy_sort(random_vector));
    }
    state.SetItemsProcessed(state.range(0));
    state.SetBytesProcessed(state.range(0)*sizeof(Node<NodeSize>));
    state.counters["items"] = state.range(0);
    state.counters["item_size"] = sizeof(Node<NodeSize>);
}
BENCHMARK_TEMPLATE(BM_vector_insert, 1)->Range(4, 1<<20);
BENCHMARK_TEMPLATE(BM_vector_insert, 8)->Range(4, 1<<20);
BENCHMARK_TEMPLATE(BM_vector_insert, 64)->Range(4, 1<<20);
BENCHMARK_TEMPLATE(BM_vector_insert, 512)->Range(4, 1<<20);

template <int NodeSize>
static void BM_list_insert(benchmark::State& state)
{
    auto random_list = gen_random_data<std::list<Node<NodeSize>>>(state.range(0));
    for (auto _ : state)
    {
        auto copy = std::list<Node<NodeSize>>{};
        benchmark::DoNotOptimize(copy = copy_sort(random_list));
    }
    state.SetItemsProcessed(state.range(0));
    state.SetBytesProcessed(state.range(0)*sizeof(Node<NodeSize>));
    state.counters["items"] = state.range(0);
    state.counters["item_size"] = sizeof(Node<NodeSize>);
}
BENCHMARK_TEMPLATE1(BM_list_insert, 1)->Range(4, 1<<20);
BENCHMARK_TEMPLATE1(BM_list_insert, 8)->Range(4, 1<<20);
BENCHMARK_TEMPLATE1(BM_list_insert, 64)->Range(4, 1<<20);
BENCHMARK_TEMPLATE1(BM_list_insert, 512)->Range(4, 1<<20);

BENCHMARK_MAIN();
//int main()
//{
//    for (auto i : gen_random_data<std::vector<int>>(8)) { std::cout << i << '\n'; }
//}