#pragma once
#include "types.hpp"

#ifdef PYBIND_INCLUDED
	#include <pybind11/numpy.h>
	#include <pybind11/pybind11.h>
#endif

namespace chm {
	#ifdef PYBIND_INCLUDED
		namespace py = pybind11;

		template<typename T>
		using NumpyArray = py::array_t<T, py::array::c_style | py::array::forcecast>;

		template<typename T>
		const T* const getNumpyPtr(const NumpyArray<T>& a) {
			return (const T* const)a.request().ptr;
		}

		template<typename T>
		size_t getNumpyXDim(const NumpyArray<T>& a) {
			return (size_t)a.request().shape[0];
		}

		template<typename T>
		size_t getNumpyYDim(const NumpyArray<T>& a) {
			return (size_t)a.request().shape[1];
		}
	#endif

	struct FloatArray {
		const uint count;
		const float* const data;

		FloatArray(const float* const data, const uint count);

		#ifdef PYBIND_INCLUDED
			FloatArray(const NumpyArray<float>& data, const size_t dim);
		#endif
	};

	class KnnResults {
		const size_t count;
		float* const distances;
		const size_t k;
		uint* const labels;
		bool owningData;

	public:
		~KnnResults();
		const uint* const getLabels() const;
		KnnResults(const KnnResults& o) = delete;
		KnnResults(KnnResults&& o) noexcept;
		KnnResults(const size_t count, const size_t k);
		KnnResults& operator=(const KnnResults&) = delete;
		KnnResults& operator=(KnnResults&& o) noexcept = delete;
		void setData(const size_t queryIdx, const size_t neighborIdx, const float distance, const uint label);

		#ifdef PYBIND_INCLUDED
			py::tuple makeTuple();
		#endif
	};
}
