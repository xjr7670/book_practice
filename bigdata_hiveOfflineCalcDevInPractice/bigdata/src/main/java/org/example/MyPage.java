package org.example;

import java.util.List;
import java.util.Map;

public class MyPage {
	private List<Map<String,Object>> list;
	private Integer fullListSize;
	private Integer pageNumber;
	private Integer objectsPerPage;
	
	public List<Map<String, Object>> getList() {
		return list;
	}
	public void setList(List<Map<String, Object>> list) {
		this.list = list;
	}
	public Integer getFullListSize() {
		return fullListSize;
	}
	public void setFullListSize(Integer fullListSize) {
		this.fullListSize = fullListSize;
	}
	public Integer getPageNumber() {
		return pageNumber;
	}
	public void setPageNumber(Integer pageNumber) {
		this.pageNumber = pageNumber;
	}
	public Integer getObjectsPerPage() {
		return objectsPerPage;
	}
	public void setObjectsPerPage(Integer objectsPerPage) {
		this.objectsPerPage = objectsPerPage;
	}
	
}
